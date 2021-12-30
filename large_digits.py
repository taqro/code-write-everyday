{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "large_digits.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOTZIH/Ecmw0yCDDvqGv6Jq",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/large_digits.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p5k0Yie00hXi",
        "outputId": "c8eb3772-a461-48d7-ad28-cdeed64b07f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 999\n",
            "27\n"
          ]
        }
      ],
      "source": [
        "a = list(input().split())\n",
        "\n",
        "A = a[0]\n",
        "B = a[1]\n",
        "\n",
        "sum_A = int(A[0]) + int(A[1]) + int(A[2])\n",
        "sum_B = int(B[0]) + int(B[1]) + int(B[2])\n",
        "\n",
        "if sum_A >= sum_B:\n",
        "  print(sum_A)\n",
        "else:\n",
        "  print(sum_B)"
      ]
    }
  ]
}