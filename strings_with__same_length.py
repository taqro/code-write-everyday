{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "strings_with _same_length.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMsJrDj/U04QmUZTQnxQ5tW",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/strings_with__same_length.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "PCqmSB4aEWGM",
        "outputId": "20063637-a225-44a9-f1ad-9a7374c5acc2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "aaaaa bbbbb\n",
            "ababababab\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N = int(input())\n",
        "\n",
        "S, T = input().split()\n",
        "\n",
        "res = \"\"\n",
        "for i in range(N):\n",
        "  res += S[i] + T[i]\n",
        "\n",
        "print(res)"
      ]
    }
  ]
}