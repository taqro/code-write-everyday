{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "how_many_ways?.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPXz6ckQUvSbRcYslQiuSyS",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/how_many_ways%3F.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jlI9vnrkUSN7",
        "outputId": "1d6be0af-8af3-4cf5-f7d3-655af0eb2991"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 297\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "n, x = map(int, input().split())\n",
        "\n",
        "sum = 0\n",
        "\n",
        "for i in range(1, n + 1):\n",
        "  for j in range(i +1, n + 1):\n",
        "    for k in range(j + 1, n + 1):\n",
        "      if i + j + k == x:\n",
        "        sum += 1\n",
        "        \n",
        "print(sum)\n"
      ]
    }
  ]
}