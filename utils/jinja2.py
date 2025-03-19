import os
from jinja2 import Environment, FileSystemLoader

jinja2_path = os.path.join("/home/ubuntu/itda_deploy_instnace", "jinja2")
env = Environment(loader=FileSystemLoader(jinja2_path))

def generate_docker_compose(subdomain:str, port:str, docker_image:str):
  template = env.get_template("docker_compose.jinja2")
  data = {
    "subdomain": subdomain,
    "port": port,
    "docker_image": docker_image
    }
  output = template.render(data)

  file_path = os.path.join("/home/ubuntu", subdomain, f'docker-compose-{subdomain}.yml')
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(output)
  return

def generate_nginx(subdomain:str, port:str):
  template = env.get_template("nginx.jinja2")
  data = {
    "subdomain": subdomain,
    "port": port
    }
  output = template.render(data)

  file_path = os.path.join("/home/ubuntu", subdomain, f'{subdomain}.soc-canvas.com')
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(output)

def generate_nginx_conf():
  template = env.get_template("nginx_conf.jinja2")
  data = {}
  output = template.render(data)

  file_path = os.path.join("/etc/nginx/conf.d", f'nginx_conf')
  with open(file_path, 'w', encoding='utf-8') as f:
    f.write(output)