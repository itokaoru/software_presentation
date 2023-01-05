# 命名規則 : (dockerhub のアカウント名)/(環境名):(バージョンタグ)
IMAGE_NAME := otamesi515/sample_env:1.0
# 命名規則 : (環境名).(使用者の名前)
CONTAINER_NAME := sample_env.ito

# サーバに IMAGE_NAME という名前の Docker イメージが作られる.
.PHONY: build
build:
	@docker build . -t $(IMAGE_NAME)

# IMAGE_NAME というイメージを元に CONTAINER_NAME という名前の Docker コンテナが起動する.
.PHONY: run
run:
	@docker run --rm -it \
          -u root \
          --name $(CONTAINER_NAME) \
          -v $(shell pwd):/var/www \
          $(IMAGE_NAME) bash