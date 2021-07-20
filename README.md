# awx-receptor-node


```bash
$ git clone https://github.com/tchellomello/awx-receptor-node.git
$ cd awx-receptor-node
$ pip install -r requirements.txt
$ ./manage makemigrations
$ ./manage migrate
$ ./manage runserver
```

Then visit the http://localhost:8000/admin to create the resources.

To display the configuration, you curl http://localhost:8000/receptor_mode/<NAME>/ or http://localhost:8000/receptor_node/<ID>/

