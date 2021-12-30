{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "正直者.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP+gkBvc8QFh5Jmn5NpnvC4",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/%E6%AD%A3%E7%9B%B4%E8%80%85.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WavBWpb9UezZ",
        "outputId": "8d96d4e0-1f49-4ed7-a1a9-275a4cc9bdf9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 11\n",
            "11\n"
          ]
        }
      ],
      "source": [
        "X, Y = map(int, input().split())\n",
        "\n",
        "if X > Y:\n",
        "  print(X)\n",
        "else:\n",
        "  print(Y)"
      ]
    }
  ]
}