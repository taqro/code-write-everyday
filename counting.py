{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "counting.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNpqAsnMgdd9kzoYENo5rxN",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/counting.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZRHdvLa_bYSF",
        "outputId": "64f4fcb8-df95-489e-ee94-c40c5f57acc5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 2\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "A, B = map(int, input().split())\n",
        "\n",
        "sum = 0\n",
        "for i in range(A, B + 1):\n",
        "  sum += 1\n",
        "\n",
        "print(sum)"
      ]
    }
  ]
}