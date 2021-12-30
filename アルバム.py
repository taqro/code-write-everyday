{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "アルバム.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMdMWp/Fr6PnmjIWlgkx6Xv",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/%E3%82%A2%E3%83%AB%E3%83%90%E3%83%A0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0EZIsvewaJ3C",
        "outputId": "0deb1fb0-d788-47a7-de72-8ba87184613f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 1\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "S, T = map(int, input().split())\n",
        "\n",
        "sum = 0\n",
        "for i in range(S, T + 1):\n",
        "  sum += 1\n",
        "\n",
        "print(sum)"
      ]
    }
  ]
}