{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "rolling_dice.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyODiz0kfAdvNnCCR+t5Oc94",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/rolling_dice.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RSucrpUsb9xm",
        "outputId": "12dbfd3c-2e33-43b1-cb01-9e721ac6b1fe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 11\n",
            "Yes\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "A, B = map(int, input().split())\n",
        "\n",
        "ans = \"No\"\n",
        "\n",
        "if A <= B <= 6 * A:\n",
        "  ans = \"Yes\"\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}