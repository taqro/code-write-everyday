{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "repression.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyON0CCY5n6CwBaOPw/n1Bgh",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/repression.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tAfAFjI5hp0d",
        "outputId": "c7a8a00b-986e-486e-b30f-3e15b829124d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 4 5\n",
            "9\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "A, B, C = map(int, input().split())\n",
        "\n",
        "max = A + B\n",
        "\n",
        "if max < A + C:\n",
        "  max = A + C\n",
        "  \n",
        "if max < B + C:\n",
        "  max = B + C\n",
        "\n",
        "print(max)"
      ]
    }
  ]
}