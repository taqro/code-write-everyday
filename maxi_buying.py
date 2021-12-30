{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "maxi_buying.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOALL57Y3vQ9TxdHth7lkUN",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/maxi_buying.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MCfNGyVqisl5",
        "outputId": "35f932eb-864a-45ee-e9f0-686de113bf30"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "191\n",
            "so-so\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N = int(input())\n",
        "\n",
        "if int(1.08 * N) < 206:\n",
        "  print(\"Yay!\")\n",
        "elif int(1.08 * N) == 206:\n",
        "  print(\"so-so\")\n",
        "else:\n",
        "  print(\":(\")\n",
        "  "
      ]
    }
  ]
}