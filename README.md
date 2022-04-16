# Control Plane - Django Example


1. Clone repository
2. Install and login using the Control Plane CLI
3. Build and push image using the command: `cpln image build --name pizza-django:0.1 --push`
4. Create a workload using this image: `cpln workload create --name pizza-django --image pizza-django:0.1 --public`
5. That's it!