{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "alloy.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOjW3Yw40NujuuwXtqRSf7d",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/alloy.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t6smmyeZYg6h",
        "outputId": "8c7f6cbb-3416-44f1-c568-a4611e008b11"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 10\n",
            "Silver\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "a = list(map(int, input().split()))\n",
        "\n",
        "ans = \"Alloy\"\n",
        "if a[0] != 0 and a[1] == 0:\n",
        "  ans = \"Gold\"\n",
        "elif a[0] == 0 and a[1] != 0:\n",
        "  ans = \"Silver\"\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}