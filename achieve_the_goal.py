{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "achieve_the_goal.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOHwyTx5L6eV9L69BWN9MeS",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/achieve_the_goal.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f-JARVSDklhz",
        "outputId": "c253cf85-cfa9-4dc1-ddaf-202b7eefa96b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4 100 60\n",
            "0 0 0\n",
            "-1\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N, K, M = map(int, input().split())\n",
        "\n",
        "A = list(map(int, input().split()))\n",
        "\n",
        "sum = 0\n",
        "for i in range(len(A)):\n",
        "  sum += A[i]\n",
        "\n",
        "res = N * M -sum\n",
        "\n",
        "if res < 0:\n",
        "  res = 0\n",
        "\n",
        "if res > K:\n",
        "  res = -1\n",
        "\n",
        "print(res)"
      ]
    }
  ]
}