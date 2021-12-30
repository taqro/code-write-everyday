{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "signed_difficulty.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPzFu5LloeTBSQD1fjd0i/E",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/signed_difficulty.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zoA1wscg9c3a",
        "outputId": "2d80cbff-f41b-4da1-db9d-bb49294b393f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12.5\n",
            "12\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "a = list(map(int, input().split(\".\")))\n",
        "\n",
        "ans = str(a[0])\n",
        "if a[1] <= 2:\n",
        "  ans += \"-\"\n",
        "elif 7 <= a[1] <= 9:\n",
        "  ans += \"+\"\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}