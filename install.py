import base64
import subprocess
import os


if __name__ == '__main__':
    script = """
        IyEvYmluL2Jhc2gKCkRCX1BBVEg9ezB9Ck9VVF9QQVRIPXsxfQoKbWtkaXIgLXAgJHt7T1VUX1BB
        VEh9fS9pcHRhYmxlCm1rZGlyIC1wICR7e09VVF9QQVRIfX0vc3MKCmJhc2U2NCAtZCAke3tEQl9Q
        QVRIfX0vREIxXzEgPiAke3tPVVRfUEFUSH19L2lwdGFibGUvY3JlYXRlX2ZvcndhcmQuc2gKYmFz
        ZTY0IC1kICR7e0RCX1BBVEh9fS9EQjFfMiA+ICR7e09VVF9QQVRIfX0vaXB0YWJsZS9yZW1vdmVf
        Zm9yd2FyZC5zaApiYXNlNjQgLWQgJHt7REJfUEFUSH19L0RCMl8xID4gJHt7T1VUX1BBVEh9fS9z
        cy9pbnN0YWxsLnNoCmJhc2U2NCAtZCAke3tEQl9QQVRIfX0vREIyXzIgPiAke3tPVVRfUEFUSH19
        L3NzL2NvbmZpZy5zaAoKY2htb2QgdSt4ICR7e09VVF9QQVRIfX0vaXB0YWJsZS9jcmVhdGVfZm9y
        d2FyZC5zaCAke3tPVVRfUEFUSH19L2lwdGFibGUvcmVtb3ZlX2ZvcndhcmQuc2ggJHt7T1VUX1BB
        VEh9fS9zcy9pbnN0YWxsLnNoICR7e09VVF9QQVRIfX0vc3MvY29uZmlnLnNoCg==
    """

    current_dir, self_dir = os.getcwd(), os.path.dirname(os.path.realpath(__file__))
    subprocess.run([base64.b64decode(script.encode()).decode().format(os.path.join(self_dir, 'data'), current_dir)], shell=True)
