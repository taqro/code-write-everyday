{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ABC_swap.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyO3D4+NwNeVM8ctI53DKirV",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/ABC_swap.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VwPTchyPJ9gY",
        "outputId": "d6f37dc7-e0fc-469c-c231-750edc4ec9b8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n",
            "3 1 2\n"
          ]
        }
      ],
      "source": [
        "X, Y, Z = map(int, input().split())\n",
        "\n",
        "a = X\n",
        "b = Y\n",
        "c = Z\n",
        "\n",
        "X = str(c)\n",
        "Y = str(a)\n",
        "Z = str(b)\n",
        "\n",
        "print(X + \" \" + Y + \" \" + Z)"
      ]
    }
  ]
}