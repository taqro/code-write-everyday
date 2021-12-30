{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "star.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMedZ98BEeKsLTi3F4DVhgF",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/star.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YShIH4YsR19L",
        "outputId": "544523ae-0295-4fc7-ffe2-88a55c417e2f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1000\n",
            "100\n"
          ]
        }
      ],
      "source": [
        "X = int(input())\n",
        "\n",
        "ans = 0\n",
        "for i in range(1, 100 + 1):\n",
        "  if (X + i) % 100 == 0:\n",
        "    ans = i\n",
        "    break\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}