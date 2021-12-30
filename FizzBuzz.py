{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "FizzBuzz.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOsHdv1EYCdHVV2zQcmAojG",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/FizzBuzz.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oaxTP07q-aOa",
        "outputId": "0d43466a-655e-4968-bfe0-547ee7c511ca"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "1\n",
            "2\n",
            "Fizz\n",
            "4\n",
            "Buzz\n",
            "Fizz\n",
            "7\n",
            "8\n",
            "Fizz\n",
            "Buzz\n",
            "11\n",
            "Fizz\n",
            "13\n",
            "14\n",
            "FizzBuzz\n"
          ]
        }
      ],
      "source": [
        "# 入力\n",
        "N = int(input())\n",
        "\n",
        "for i in range(1, N + 1):\n",
        "  if i % 3 == 0 and i % 5 == 0:\n",
        "    print(\"FizzBuzz\")\n",
        "  elif i % 3 == 0:\n",
        "    print(\"Fizz\")\n",
        "  elif i % 5 == 0:\n",
        "    print(\"Buzz\")\n",
        "  else:\n",
        "    print(i)\n"
      ]
    }
  ]
}