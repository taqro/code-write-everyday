{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "conins.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMF8nFmUcm3nKj3Vw7acqRr",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/conins.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CBM55u9JdHfl",
        "outputId": "d7ef7b76-ab35-4f53-e1de-1e1fbbd868bd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "500円玉の枚数を入力\n",
            "10\n",
            "100円玉の枚数を入力\n",
            "20\n",
            "50円玉の枚数を入力\n",
            "10\n",
            "合計金額を入力（50の倍数）\n",
            "1050\n",
            "11\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "print(\"500円玉の枚数を入力\")\n",
        "A = int(input())\n",
        "print(\"100円玉の枚数を入力\")\n",
        "B = int(input())\n",
        "print(\"50円玉の枚数を入力\")\n",
        "C = int(input())\n",
        "\n",
        "print(\"合計金額を入力（50の倍数）\")\n",
        "X = int(input())\n",
        "\n",
        "# 合計金額をXにできる通り数\n",
        "sum = 0\n",
        "\n",
        "for i in range(A):\n",
        "  for j in range(B):\n",
        "    for k in range(C):\n",
        "      total = 500 * i + 100 * j + 50 * k\n",
        "      if total == X:\n",
        "        sum += 1\n",
        "\n",
        "print(sum)"
      ]
    }
  ]
}