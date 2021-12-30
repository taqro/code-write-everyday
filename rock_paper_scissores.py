{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "rock_paper_scissores.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNPWlijclD4Yi2nk30oCuat",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/rock_paper_scissores.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YAnSpDZ8kmE6",
        "outputId": "42d20eda-1700-41fa-fee5-946f40da788e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 0\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "x, y = map(int, input().split())\n",
        "\n",
        "if (x == 0 and y == 1) or (x == 1 and y == 0):\n",
        "  print(2)\n",
        "elif (x == 2 and y == 0) or (x == 0 and y == 2):\n",
        "  print(1)\n",
        "elif (x == 1 and y == 2) or (x == 2 and y == 1):\n",
        "  print(0)\n",
        "elif x == y:\n",
        "  print(x)"
      ]
    }
  ]
}