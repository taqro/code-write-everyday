{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "bitwise_exclusive_or.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyO6TSgoDM9ZvxqcCMb6FYUN",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/bitwise_exclusive_or.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lf6Q0LOnCBb1",
        "outputId": "6fbd84a7-42b5-4dd4-e061-b1577e4546a8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 12\n",
            "6\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "A, B = map(int, input().split())\n",
        "\n",
        "ans = 0\n",
        "for i in range(256):\n",
        "  if bin(A ^ i ) == bin(B):\n",
        "    ans = i\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}