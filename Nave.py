import pygame
from ElementoJogo import ElementoJogo

class Nave(ElementoJogo):
    def __init__(
            self,
            largura_tela,
            altura_tela,
            velocidade=5,
            cor=(0, 255, 100)):
        
        # Inicializa a classe base com posição inicial centralizada embaixo
        super().__init__(
            x=largura_tela // 2 - 20,
            y=altura_tela - 60,
            largura=40,
            altura=40,
            cor=cor,
            velocidade=velocidade
        )
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.vel_x = 0
        self.tiros = []  # Lista que guardará os tiros ativos
        self.velocidade_tiro = 10

    def processar_evento(self, evento):
        """Controla os eventos de teclado para movimentação e disparo."""
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.vel_x = -self.velocidade
            elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.vel_x = self.velocidade
            elif evento.key == pygame.K_SPACE:
                self.atirar()

        elif evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_a) and self.vel_x < 0:
                self.vel_x = 0
            elif evento.key in (pygame.K_RIGHT, pygame.K_d) and self.vel_x > 0:
                self.vel_x = 0

    def mover(self):
        """Aplica o deslocamento horizontal e trava nas bordas da tela."""
        self.rect.x += self.vel_x

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.largura_tela:
            self.rect.right = self.largura_tela

    def atirar(self):

        largura_tiro = 4
        altura_tiro = 10

        tiro = pygame.Rect(
            0,
            0,
            largura_tiro,
            altura_tiro
        )

        tiro.centerx = self.rect.centerx
        tiro.bottom = self.rect.top

        self.tiros.append(tiro)

    def atualizar_tiros(self):

        for tiro in self.tiros:
            tiro.y -= self.velocidade_tiro

        self.tiros = [
            tiro for tiro in self.tiros
            if tiro.bottom >= 0
        ]

    def atualizar(self):
        self.mover()
        self.atualizar_tiros()

    def desenhar(self, tela, vidas=3):
        # Cores conforme o estado de dano
        if vidas >= 3:
            cor_corpo = self.cor
            cor_asas = (20, 110, 180)

        elif vidas == 2:
            cor_corpo = (255, 170, 40)
            cor_asas = (180, 90, 20)

        else:
            cor_corpo = (255, 70, 70)
            cor_asas = (140, 30, 30)

        centro_x = self.rect.centerx
        topo = self.rect.top
        base = self.rect.bottom
        esquerda = self.rect.left
        direita = self.rect.right

        # Animação simples dos propulsores
        oscilacao = (pygame.time.get_ticks() // 100) % 2

        if oscilacao == 0:
            comprimento_chama = 7
        else:
            comprimento_chama = 11

        # Propulsores não aparecem no Game Over
        if vidas > 0:
            # Chama esquerda
            pygame.draw.polygon(
                tela,
                (255, 100, 20),
                [
                    (centro_x - 9, base - 5),
                    (centro_x - 4, base - 5),
                    (
                        centro_x - 6,
                        base + comprimento_chama
                    )
                ]
            )

            # Chama direita
            pygame.draw.polygon(
                tela,
                (255, 100, 20),
                [
                    (centro_x + 4, base - 5),
                    (centro_x + 9, base - 5),
                    (
                        centro_x + 6,
                        base + comprimento_chama
                    )
                ]
            )

            # Parte interna amarela das chamas
            pygame.draw.line(
                tela,
                (255, 240, 100),
                (centro_x - 6, base - 4),
                (
                    centro_x - 6,
                    base + comprimento_chama - 3
                ),
                2
            )

            pygame.draw.line(
                tela,
                (255, 240, 100),
                (centro_x + 6, base - 4),
                (
                    centro_x + 6,
                    base + comprimento_chama - 3
                ),
                2
            )

        # Asa esquerda
        asa_esquerda = [
            (centro_x - 5, topo + 14),
            (esquerda + 2, base - 4),
            (centro_x - 5, base - 10)
        ]

        pygame.draw.polygon(
            tela,
            cor_asas,
            asa_esquerda
        )

        # Asa direita
        asa_direita = [
            (centro_x + 5, topo + 14),
            (direita - 2, base - 4),
            (centro_x + 5, base - 10)
        ]

        pygame.draw.polygon(
            tela,
            cor_asas,
            asa_direita
        )

        # Corpo principal
        corpo_nave = [
            (centro_x, topo),
            (centro_x - 8, base - 7),
            (centro_x, base - 12),
            (centro_x + 8, base - 7)
        ]

        pygame.draw.polygon(
            tela,
            cor_corpo,
            corpo_nave
        )

        # Contorno do corpo
        pygame.draw.polygon(
            tela,
            (220, 240, 255),
            corpo_nave,
            2
        )

        # Cabine
        cabine = pygame.Rect(
            centro_x - 5,
            topo + 9,
            10,
            13
        )

        pygame.draw.ellipse(
            tela,
            (80, 220, 255),
            cabine
        )

        pygame.draw.ellipse(
            tela,
            (220, 255, 255),
            cabine,
            2
        )

        # Motores
        pygame.draw.rect(
            tela,
            (80, 80, 95),
            pygame.Rect(
                centro_x - 9,
                base - 9,
                5,
                6
            )
        )

        pygame.draw.rect(
            tela,
            (80, 80, 95),
            pygame.Rect(
                centro_x + 4,
                base - 9,
                5,
                6
            )
        )

        # Dano moderado
        if vidas == 2:
            pygame.draw.line(
                tela,
                (55, 45, 40),
                (centro_x, topo + 18),
                (centro_x + 7, base - 8),
                3
            )

        # Dano crítico
        elif vidas <= 1:
            pygame.draw.line(
                tela,
                (40, 30, 30),
                (centro_x, topo + 6),
                (centro_x - 7, base - 8),
                3
            )

            pygame.draw.line(
                tela,
                (40, 30, 30),
                (centro_x, topo + 18),
                (centro_x + 8, base - 7),
                3
            )

            pygame.draw.circle(
                tela,
                (35, 35, 35),
                (centro_x, topo + 22),
                4
            )

        # Tiros da nave
        for tiro in self.tiros:
            pygame.draw.rect(
                tela,
                (255, 255, 100),
                tiro
            )