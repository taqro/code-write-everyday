{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "twiblr.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNDLibxh8W8De+uTn6knXfv",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/twiblr.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dWbY2ymGP_Bu",
        "outputId": "48887499-14fd-439c-b39e-7d5d353f07d2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10000 0\n",
            "20100\n"
          ]
        }
      ],
      "source": [
        "A, B = map(int, input().split())\n",
        "\n",
        "ans = 2 * A + 100 - B\n",
        "print(ans)"
      ]
    }
  ]
}