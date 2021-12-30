{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "rotate.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPUtos5b31UM1aykH+Mf0C2",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/rotate.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aT2D8ZgP_tFy",
        "outputId": "3feed2dc-1e06-4853-df12-618a6c0cb41b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "aab\n",
            "aba\n"
          ]
        }
      ],
      "source": [
        "S = list(input())\n",
        "\n",
        "a = S[0]\n",
        "\n",
        "S[0] = S[1]\n",
        "S[1] = S[2]\n",
        "S[2] = a\n",
        "\n",
        "S = S[0] + S[1] + S[2]\n",
        "\n",
        "print(S)"
      ]
    }
  ]
}