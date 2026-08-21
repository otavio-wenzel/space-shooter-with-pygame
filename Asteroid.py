import random
import pygame
import math
from ElementoJogo import ElementoJogo


class Asteroid(ElementoJogo):
    def __init__(
            self,
            largura_tela,
            altura_tela,
            velocidade=5,
            cor=(200, 50, 50)):
        
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.raio = 20

        super().__init__(
            x=0,
            y=0,
            largura=self.raio * 2,
            altura=self.raio * 2,
            cor=cor,
            velocidade=velocidade
        )
        self.iniciar_status()

    def iniciar_status(self):
        # =========================================================================
        # TODO 3 (Alunos):
        # - Sortear uma posição X aleatória dentro dos limites da tela
        # - Posicionar o Y acima da tela (ex: entre -150 e -50)
        # - Sortear uma velocidade de queda aleatória (ex: entre 3 e 7)
        # =========================================================================
        
        self.rect.x = random.randint(
            0,
            self.largura_tela - self.rect.width
        )

        self.rect.y = random.randint(-150, -50)

        self.velocidade = random.randint(2, 4)

        # Rotação inicial aleatória
        self.angulo = random.uniform(0, 360)

        # Pode girar para a esquerda ou para a direita
        self.velocidade_rotacao = random.choice(
            [-2.0, -1.5, 1.5, 2.0]
        )

    def mover(self):
        self.rect.y += self.velocidade

        self.angulo += self.velocidade_rotacao
        self.angulo %= 360

        # Reinicia quando sair completamente pelo fundo
        if self.rect.top > self.altura_tela:
            self.iniciar_status()

    def desenhar(self, tela):
        centro_x = self.rect.centerx
        centro_y = self.rect.centery

        angulo_inicial = math.radians(self.angulo)

        # Variações no raio produzem o formato irregular
        variacoes_raio = [
            1.00,
            0.82,
            0.95,
            0.78,
            1.00,
            0.86,
            0.94,
            0.80,
            0.98,
            0.84
        ]

        pontos = []
        quantidade_pontos = len(variacoes_raio)

        for indice, variacao in enumerate(variacoes_raio):
            angulo_ponto = (
                angulo_inicial
                + (2 * math.pi * indice / quantidade_pontos)
            )

            raio_atual = self.raio * variacao

            x = centro_x + math.cos(angulo_ponto) * raio_atual
            y = centro_y + math.sin(angulo_ponto) * raio_atual

            pontos.append(
                (int(x), int(y))
            )

        # Corpo do asteroide
        pygame.draw.polygon(
            tela,
            (105, 95, 90),
            pontos
        )

        # Contorno externo
        pygame.draw.polygon(
            tela,
            (185, 170, 155),
            pontos,
            2
        )

        # Função interna para rotacionar as crateras
        def rotacionar_posicao(deslocamento_x, deslocamento_y):
            cosseno = math.cos(angulo_inicial)
            seno = math.sin(angulo_inicial)

            x_rotacionado = (
                deslocamento_x * cosseno
                - deslocamento_y * seno
            )

            y_rotacionado = (
                deslocamento_x * seno
                + deslocamento_y * cosseno
            )

            return (
                int(centro_x + x_rotacionado),
                int(centro_y + y_rotacionado)
            )

        # Posições das crateras
        cratera_grande = rotacionar_posicao(-6, -4)
        cratera_media = rotacionar_posicao(7, 2)
        cratera_pequena = rotacionar_posicao(-1, 9)

        # Cratera grande
        pygame.draw.circle(
            tela,
            (60, 55, 55),
            cratera_grande,
            5
        )

        pygame.draw.circle(
            tela,
            (135, 120, 110),
            cratera_grande,
            5,
            1
        )

        # Cratera média
        pygame.draw.circle(
            tela,
            (65, 60, 60),
            cratera_media,
            3
        )

        pygame.draw.circle(
            tela,
            (140, 125, 115),
            cratera_media,
            3,
            1
        )

        # Cratera pequena
        pygame.draw.circle(
            tela,
            (55, 50, 50),
            cratera_pequena,
            2
        )