{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "round_decimals.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNORT5BYrJpU7baENTj7bD/",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/round_decimals.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ys5MVWF29mVi",
        "outputId": "6ce934ba-e4b9-4cee-9175-54ae3f4f318f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.000\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "X = input()\n",
        "\n",
        "Y, Z =  X.split(\".\")\n",
        "\n",
        "Z = list(Z)\n",
        "\n",
        "res = 0\n",
        "if int(Z[0]) < 5:\n",
        "  res = int(Y)\n",
        "elif int(Z[0]) >= 5:\n",
        "  res = int(Y) + 1\n",
        "\n",
        "print(res)"
      ]
    }
  ]
}