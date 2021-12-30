{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "payment.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMdtjbrPPXbgcoe5+SvV8Z5",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/payment.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EjVmiE4vyh01",
        "outputId": "8154d66d-d862-4d7d-8a24-70da9a4f7880"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1900\n",
            "100\n"
          ]
        }
      ],
      "source": [
        "N = int(input())\n",
        "\n",
        "ans = 0\n",
        "if N % 1000 == 0:\n",
        "  ans = 0\n",
        "else:\n",
        "  ans = 1000 - N % 1000\n",
        "\n",
        "print(ans)"
      ]
    }
  ]
}