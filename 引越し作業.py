{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "引越し作業.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPjiIjCrlFfldiu/6D0qvyF",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/%E5%BC%95%E8%B6%8A%E3%81%97%E4%BD%9C%E6%A5%AD.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ycKfl8XFaww_",
        "outputId": "b6e24c1a-a1d3-44c4-c929-c36fb77e6f03"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "N = int(input())\n",
        "\n",
        "if N % 2 == 0:\n",
        "  print(N // 2)\n",
        "else:\n",
        "  print(N // 2 + 1)"
      ]
    }
  ]
}