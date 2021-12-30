{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "new_generation_ABC.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOmaHpqdbA4BF4ognpxxWAV",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/new_generation_ABC.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vbirbmFZA53b",
        "outputId": "00fba4c3-8350-4c7b-fd7a-48327da8aee4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "211\n",
            "6\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N = int(input())\n",
        "\n",
        "ans = 0\n",
        "if N <= 125:\n",
        "  ans = 4\n",
        "elif 126 <= N <= 211:\n",
        "  ans = 6\n",
        "elif 212 <= N <= 214:\n",
        "  ans = 8\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}