{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "cabbages.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMY5RY4AN0GlbdjXfj8tMiZ",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/cabbages.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jsb0woBeaQxj",
        "outputId": "967fedc0-b0eb-4f04-d441-99b95bf1867c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 10 100 1\n",
            "1000\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N, A, X, Y = map(int, input().split())\n",
        "\n",
        "ans = 0\n",
        "\n",
        "if N <= A:\n",
        "  ans = N * X\n",
        "elif A < N:\n",
        "  ans = A * X + (N - A) * Y\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}