{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "takoyaki.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOSfYGa6FGw6PVjWc0Ew36j",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/takoyaki.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Eh56MdfqvH0M",
        "outputId": "46efafd1-c459-4108-fc22-b04dd4b4c75e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1000 1 1000\n",
            "1000000\n"
          ]
        }
      ],
      "source": [
        "N, X, T = map(int, input().split())\n",
        "\n",
        "\n",
        "for i in range(1000 + 1):\n",
        "  if N <= X * i:\n",
        "    print(i  * T)\n",
        "    break"
      ]
    }
  ]
}