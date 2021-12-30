{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "five_variables.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN3N0efn6Kgma5NnL/ruYYa",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/five_variables.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zA8PwJrL0Q66",
        "outputId": "9c305c9f-bf60-4f4c-a435-2236afba5618"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 0 4 5\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "a = list(map(int, input().split()))\n",
        "\n",
        "for i in range(len(a)):\n",
        "  if a[i] == 0:\n",
        "    print(i + 1)\n",
        "    break"
      ]
    }
  ]
}