import pygame
from Nave import Nave
from Asteroid import Asteroid


class Jogo:
    def __init__(self, largura=800, altura=600):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Space Shooter - Projeto Base")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.rodando = True
        self.pontos = 0
        self.vidas_iniciais = 3
        self.vidas = self.vidas_iniciais
        self.fonte = pygame.font.Font(None, 36)
        self.fonte_game_over = pygame.font.Font(None, 72)
        self.fonte_instrucao = pygame.font.Font(None, 32)

        # Elementos do jogo
        self.nave = Nave(self.largura, self.altura)
        self.game_over = False
        self.posicao_inicial_nave = self.nave.rect.copy()
        self.asteroide = Asteroid(self.largura, self.altura)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

            elif self.game_over:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        self.reiniciar_partida()

            else:
                self.nave.processar_evento(evento)

    def checar_colisoes(self):
      
        # Tiro vs Asteroide
        for tiro in self.nave.tiros[:]:
            if tiro.colliderect(self.asteroide.rect):
                self.nave.tiros.remove(tiro)

                asteroide_destruido = self.asteroide.receber_dano()

                if asteroide_destruido:
                    self.pontos += 1
                    self.asteroide.iniciar_status()

                break

        # Asteroide vs Nave
        if self.nave.rect.colliderect(self.asteroide.rect):
            self.vidas -= 1
            self.nave.vel_x = 0

            if self.vidas <= 0:
                self.game_over = True
            else:
                self.nave.rect = self.posicao_inicial_nave.copy()
                self.nave.tiros.clear()
                self.asteroide.iniciar_status()

    def atualizar(self):
        if self.game_over:
            return
        
        self.nave.atualizar()
        self.asteroide.mover()
        self.checar_colisoes()

    def desenhar(self):
        # Fundo da tela
        self.tela.fill((15, 15, 25))

        # Elementos do jogo
        self.nave.desenhar(self.tela, self.vidas)
        self.asteroide.desenhar(self.tela)

        # Tamanho atual da tela
        largura_tela, altura_tela = self.tela.get_size()

        # Pontuação no canto superior esquerdo
        texto_pontos = self.fonte.render(
            f"Pontos: {self.pontos}",
            True,
            (255, 255, 255)
        )

        self.tela.blit(texto_pontos, (20, 20))

        # Vidas no canto superior direito
        texto_vidas = self.fonte.render(
            f"Vidas: {self.vidas}",
            True,
            (255, 100, 100)
        )

        rect_vidas = texto_vidas.get_rect(
            topright=(largura_tela - 20, 20)
        )

        self.tela.blit(texto_vidas, rect_vidas)

        # Tela exibida somente quando a partida terminar
        if self.game_over:
            camada_escura = pygame.Surface(
                (largura_tela, altura_tela),
                pygame.SRCALPHA
            )

            camada_escura.fill((0, 0, 0, 180))
            self.tela.blit(camada_escura, (0, 0))

            texto_game_over = self.fonte_game_over.render(
                "GAME OVER",
                True,
                (255, 80, 80)
            )

            texto_reiniciar = self.fonte_instrucao.render(
                "Pressione R para reiniciar",
                True,
                (255, 255, 255)
            )

            rect_game_over = texto_game_over.get_rect(
                center=(
                    largura_tela // 2,
                    altura_tela // 2 - 30
                )
            )

            rect_reiniciar = texto_reiniciar.get_rect(
                center=(
                    largura_tela // 2,
                    altura_tela // 2 + 35
                )
            )

            self.tela.blit(texto_game_over, rect_game_over)
            self.tela.blit(texto_reiniciar, rect_reiniciar)

        # Exibe o frame completo
        pygame.display.flip()

    def executar(self):
        while self.rodando:
            self.clock.tick(self.fps)
            self.processar_eventos()
            self.atualizar()
            self.desenhar()

        pygame.quit()

    def reiniciar_partida(self):
        self.pontos = 0
        self.vidas = self.vidas_iniciais
        self.game_over = False

        self.nave.rect = self.posicao_inicial_nave.copy()
        self.nave.vel_x = 0
        self.nave.tiros.clear()

        self.asteroide.iniciar_status()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()