{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "box.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOhs3wq+zUKV7g/ShYgWwfR",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/box.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QBNpWp7hSmEH",
        "outputId": "e204a239-8a9e-43dc-e811-9bd99d4e3f01"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 2 1\n",
            "99\n"
          ]
        }
      ],
      "source": [
        "N, A, B = map(int, input().split())\n",
        "\n",
        "ans = N - A + B\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}