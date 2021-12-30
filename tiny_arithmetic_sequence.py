{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "tiny_arithmetic_sequence.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPITP90e9j85wOu3jhNJ4c2",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/tiny_arithmetic_sequence.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WlxJaN0An1pq",
        "outputId": "c2153a15-4bb0-4110-b71f-03ae72e9727e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 5 5\n",
            "Yes\n"
          ]
        }
      ],
      "source": [
        "a = list(map(int, input().split()))\n",
        "\n",
        "a.sort()\n",
        "\n",
        "if a[0] - a[1] == a[1] - a[2]:\n",
        "  print(\"Yes\")\n",
        "else:\n",
        "  print(\"No\")"
      ]
    }
  ]
}