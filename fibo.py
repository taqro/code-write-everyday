{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "fibo.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMZ083DJ5yHGu72ZqmvPfxp",
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
        "<a href=\"https://colab.research.google.com/github/taqro/code-write-everyday/blob/master/fibo.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xMLKJkRej84i",
        "outputId": "236fbd42-37a8-4ddd-b750-f2ad6ce542a7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[-1, -1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]\n",
            "50\n",
            "2項目：1\n",
            "3項目：2\n",
            "4項目：3\n",
            "5項目：5\n",
            "6項目：8\n",
            "7項目：13\n",
            "8項目：21\n",
            "9項目：34\n",
            "10項目：55\n",
            "11項目：89\n",
            "12項目：144\n",
            "13項目：233\n",
            "14項目：377\n",
            "15項目：610\n",
            "16項目：987\n",
            "17項目：1597\n",
            "18項目：2584\n",
            "19項目：4181\n",
            "20項目：6765\n",
            "21項目：10946\n",
            "22項目：17711\n",
            "23項目：28657\n",
            "24項目：46368\n",
            "25項目：75025\n",
            "26項目：121393\n",
            "27項目：196418\n",
            "28項目：317811\n",
            "29項目：514229\n",
            "30項目：832040\n",
            "31項目：1346269\n",
            "32項目：2178309\n",
            "33項目：3524578\n",
            "34項目：5702887\n",
            "35項目：9227465\n",
            "36項目：14930352\n",
            "37項目：24157817\n",
            "38項目：39088169\n",
            "39項目：63245986\n",
            "40項目：102334155\n",
            "41項目：165580141\n",
            "42項目：267914296\n",
            "43項目：433494437\n",
            "44項目：701408733\n",
            "45項目：1134903170\n",
            "46項目：1836311903\n",
            "47項目：2971215073\n",
            "48項目：4807526976\n",
            "49項目：7778742049\n"
          ]
        }
      ],
      "source": [
        "# メモを宣言\n",
        "memo = []\n",
        "\n",
        "# フィボナッチ関数\n",
        "def fibo(N):\n",
        "  # ベースケース\n",
        "  if N == 0 :\n",
        "    return 0\n",
        "  elif N == 1 :\n",
        "    return 1\n",
        "  \n",
        "  # メモをチェック\n",
        "  if memo[N] != -1:\n",
        "    return memo[N]\n",
        "  \n",
        "  # 答えをメモ化しながら、再帰呼び出し\n",
        "  memo[N] = fibo(N - 1) + fibo (N - 2)\n",
        "  return memo[N]\n",
        "\n",
        "# -1で初期化\n",
        "memo = [-1] * 50\n",
        "\n",
        "# fibo(49)を呼び出す\n",
        "fibo(49)\n",
        "\n",
        "print(memo)\n",
        "\n",
        "print(len(memo))\n",
        "\n",
        "# memo[0], ... ,[49]に答えが格納されている\n",
        "for i in range(2, len(memo)):\n",
        "    print(str(i) + \"項目：\"  + str(memo[i]))\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "EMviCwsvmcYn"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}