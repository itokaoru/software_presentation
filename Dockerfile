# 1. dockerhub でベースにしたいイメージを選択 (tensorflow, pytorch, ...)
FROM python:3.9.14

# 2. コンテナの作業場所の決定
ENV WORKSPACE /var/www
WORKDIR $WORKSPACE

# 4. Poerty のインストール
RUN pip install poetry
ENV PATH /root/.poetry/bin:$PATH

# 5. 2 つのライブラリ管理ファイルをコンテナにコピー (初めて環境構築する際は, ここはコメントアウト)
COPY pyproject.toml $WORKSPACE
COPY poetry.lock $WORKSPACE

# apt の package などの必要なものをインストール
# RUN apt-get update -y && apt-get upgrade -y
#     apt-get install libgl1-mesa-dev -y

# 6. Poetry でインストールできないライブラリをインストール (任意)
RUN pip install --ignore-installed django==3.2
RUN pip install django-bootstrap5
RUN pip install Pillow
# # 7. Poetry によるライブラリの依存関係の解決 (初めて環境構築する際は, ここはコメントアウト)
# RUN poetry config virtualenvs.create false && \
#     pip install --upgrade pip && \
#     pip install -U setuptools && \
#     poetry install -n

# nvidia の version に応じた pytorch のインストール
# RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

# 8. エントリーポイントの指定
CMD ["python"]