{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chinchirorin.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMemXNOBqUQOe1n/hA4Pl82",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/chinchirorin.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TRAUkpPbl8To",
        "outputId": "3ba7e149-81e5-41e7-dec7-b266711206cc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4 5 6\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "a, b, c = map(int, input().split())\n",
        "\n",
        "if a == b:\n",
        "  print(c)\n",
        "elif b == c:\n",
        "  print(a)\n",
        "elif c == a:\n",
        "  print(b)\n",
        "else:\n",
        "  print(0)"
      ]
    }
  ]
}