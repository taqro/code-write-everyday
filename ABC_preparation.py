{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ABC_preparation.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPNBpkWwT0mIBnlu1EOgNfS",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/ABC_preparation.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1Ug0XOLx2vfP",
        "outputId": "1588bbfa-a264-4d80-dce2-e658853bf42b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 100 1 100\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "a = list(map(int, input().split()))\n",
        "\n",
        "a.sort()\n",
        "\n",
        "print(a[0])"
      ]
    }
  ]
}