{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "I_scream.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOlCTApDPnX3TIMlGe2HTd3",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/I_scream.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sKRM-zQJPqjf",
        "outputId": "f0a1d5c4-21fc-48d4-f467-112157a83666"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 0\n",
            "4\n"
          ]
        }
      ],
      "source": [
        "A, B =map(int, input().split())\n",
        "\n",
        "\n",
        "if 15 <= A + B and 8 <= B:\n",
        "  print(\"1\")\n",
        "elif 10 <= A + B and 3 <= B:\n",
        "  print(\"2\")\n",
        "elif 3 <= A + B:\n",
        "  print(\"3\")\n",
        "else:\n",
        "  print(\"4\")"
      ]
    }
  ]
}