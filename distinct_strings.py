{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "distinct_strings.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOl+V+IDc5zSBerECIYYv+Z",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/distinct_strings.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gnCmREWWCD6h",
        "outputId": "e3252938-ba57-4e84-c80e-dfe491cdb24a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "xyz\n",
            "6\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "S = list(input())\n",
        "\n",
        "sum = 0\n",
        "for i in range(1, 3):\n",
        "  if S[0] == S[i]:\n",
        "      sum += 1\n",
        "if S[1] == S[2]:\n",
        "  sum += 1\n",
        "res = 0\n",
        "if sum == 3:\n",
        "  res = 1\n",
        "if sum == 1:\n",
        "  res = 3\n",
        "if sum == 0:\n",
        "  res = 6\n",
        "\n",
        "print(res)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "pXZhbaSiD88J"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}