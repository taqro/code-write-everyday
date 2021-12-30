{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "10_yen_stamp.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOt0LT1b7e8mnUenT6eh894",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/10_yen_stamp.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0mjud_pfMB9a",
        "outputId": "5a30108c-83ee-4434-da02-236c68b8a414"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1000 63\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "X, Y = map(int, input().split())\n",
        "\n",
        "ans = 0\n",
        "for i in range(1000):\n",
        "  if Y <= X + 10 * i:\n",
        "      ans = i\n",
        "      break\n",
        "      \n",
        "print(ans)"
      ]
    }
  ]
}