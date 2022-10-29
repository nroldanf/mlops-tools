import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(cfg.db.driver)
    print(cfg["db"]["user"])

if __name__ == "__main__":
    my_app()