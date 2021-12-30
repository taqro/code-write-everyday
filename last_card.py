{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "last_card.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNUx+7rY5JTuzd/8Qmx6uIx",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/last_card.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9AG73pn6c1j6",
        "outputId": "2c63576b-a548-4e2c-d0cd-4117f99421a2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 100 1\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N, K, A = map(int, input().split())\n",
        "\n",
        "res = A - 1 + K % N \n",
        "\n",
        "if res > N:\n",
        "  res -= N \n",
        "\n",
        "if N == 1: #1の場合は例外\n",
        "  res = 1\n",
        "\n",
        "print(res)"
      ]
    }
  ]
}