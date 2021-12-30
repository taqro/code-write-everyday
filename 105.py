{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "105.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMVGNo0qVRaf9U621fSSpJZ",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/105.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2tBnGqeRZari",
        "outputId": "654b16b1-1eb5-4508-de9d-8671e8d83678"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "105\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "N = int(input())\n",
        "\n",
        "sum_1 = 0\n",
        "sum_2 = 0\n",
        "\n",
        "for i in range(1, N + 1):\n",
        "  \n",
        "  if i % 2 == 0:\n",
        "    continue\n",
        "  for j in range(1, N + 1):\n",
        "    if i % j == 0:\n",
        "      sum_1 += 1\n",
        "  if sum_1 == 8:\n",
        "    sum_2 += 1\n",
        "  sum_1 = 0\n",
        "\n",
        "print(sum_2)\n"
      ]
    }
  ]
}