{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "we_love_golf.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP89lMCC0My9KerBjfLa3n6",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/we_love_golf.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0GDUJD2THK3A",
        "outputId": "0fbcf4bc-189a-455b-99d5-586ade44f8e7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "5 7\n",
            "NG\n"
          ]
        }
      ],
      "source": [
        "K = int(input())\n",
        "A, B = map(int, input().split())\n",
        "\n",
        "ans = \"NG\"\n",
        "for i in range(A, B + 1):\n",
        "  if i % K == 0:\n",
        "    ans = \"OK\"\n",
        "    break\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}