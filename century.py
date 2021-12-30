{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "century.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMM3KirAehjECibTZ7tLdCn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/century.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vFRwJ0LBouAa",
        "outputId": "346ff635-666b-4df3-f2db-462303a29410"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "200\n",
            "2\n"
          ]
        }
      ],
      "source": [
        "N = int(input())\n",
        "\n",
        "ans = int(N / 100 + 1)\n",
        "\n",
        "if N % 100 == 0:\n",
        "  ans = int(N / 100)\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}