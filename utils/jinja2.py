import os
from jinja2 import Environment, FileSystemLoader

def generate_docker_compose(subdomain:str, port:str, docker_image:str):
  jinja2_path = os.path.join(os.getenv("DEPLOY_PATH"), "jinja2")
  env = Environment(loader=FileSystemLoader(jinja2_path))
  template = env.get_template("docker_compose.jinja2")
  data = {
    "subdomain": subdomain,
    "port": port,
    "docker_image": docker_image
    }
  output = template.render(data)

  file_path = os.path.join(os.getcwd(), "docker", f'docker-compose-{subdomain}.yml')
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(output)
  return

def generate_nginx(subdomain:str, port:str):
  jinja2_path = os.path.join(os.getenv("DEPLOY_PATH"), "jinja2")
  env = Environment(loader=FileSystemLoader(jinja2_path))
  template = env.get_template("nginx.jinja2")
  data = {
    "subdomain": subdomain,
    "port": port
    }
  output = template.render(data)

  file_path = os.path.join(os.getcwd(), f'{subdomain}.soc-canvas.com')
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(output)