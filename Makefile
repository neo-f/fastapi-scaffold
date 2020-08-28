DATE    ?= $(shell date +%FT%T%z)
# DATE    ?= $(shell date -u '+%Y-%m-%d %H:%M:%S %Z')

# 获取当前 git 中版号
VERSION ?= $(shell git describe --tags --always --dirty --match=v* 2> /dev/null || \
			cat $(CURDIR)/.version 2> /dev/null || echo v0)

# 0,1 是否显示日志命令
V = 0
Q = $(if $(filter 1,$V),,@)
M = $(shell printf "\033[34;1m▶\033[0m")

# 默认
.PHONY: all
all: help

.PHONY: dep
dep: ; $(info $(M) 更新所有依赖版本) @ ## 更新依赖版本
	$Q pip-compile requirements/base.in --no-emit-index-url --no-header -U -i https://mirrors.aliyun.com/pypi/simple/ > requirements/base.txt
	$Q pip-compile requirements/production.in --no-emit-index-url --no-header -U -i https://mirrors.aliyun.com/pypi/simple/ > requirements/production.txt
	$Q pip-compile requirements/local.in --no-emit-index-url --no-header -U -i https://mirrors.aliyun.com/pypi/simple/ > requirements/local.txt

.PHONY: help
help: ; $(info $(M) 帮助:)	@ ## 显示帮助信息
	@grep -hE '^[ a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-17s\033[0m %s\n", $$1, $$2}'

.PHONY: version
version: ; $(info $(M) 当前仓库 Git 版本:)	@ ## 显示当前仓库 Git 版本
	@echo $(VERSION)
