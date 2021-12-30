{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "81.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOaMfr9DWl5ZWGu9TzNJkDq",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/81.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OYURvXl-q5so",
        "outputId": "0e946d82-d32a-4248-eb64-bd54b23e888f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "50\n",
            "No\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N = int(input())\n",
        "\n",
        "res = \"No\"\n",
        "\n",
        "for i in range(1, 10):\n",
        "  for j in range(1, 10):\n",
        "    if i * j == N:\n",
        "      res = \"Yes\"\n",
        "\n",
        "print(res)\n"
      ]
    }
  ]
}