
# peter91peter91_infra


#HW-07 (lesson-09).

�������:
������ IP ��� �������� � ����������� � ���� �������� �������. ��� ����� ��������� ������� yandex_vpc_network � yandex_vpc_subnet � ���������������� ����� main.tf.
���������� ��� ��������� �������,���

������� �� � ���������� � ��������� ��������, 
����������� ���������� ������������ �����������

������� ���� vpc.tf, � ������� ������� ����������� ���� � �������, ������� ��������� ��� ���� ��������� ����� ����,
����������� ���������� ������������ �����������

������� ������������ �� 3 ������. ��������� output ���������� �� �����.  �������� ������ �������� ���.
����������� ���������� ������������ �����������


������� �������������� ��� ���� ��������� (stage � prod), ��������� ��������� ������.
����������� ���������� ������������ �����������

-------------
��������� �������� ����� ����� � ��������� ������� (remote backends) ��� ��������� stage � prod
����������� ��������� ���������� ������������ ������������, ����� ��������� ������ ����������

-------------
�������� ����������� provisioner � ������ ��� ������ � ������ ����������.


����������� ����������� ���������� provisioner � ����������� �� �������� ����������
resource "null_resource" "app" {
  count = var.prov ? 1 : 0
  triggers = {
    cluster_instance_ids = yandex_compute_instance.app.id
  }

�������� ���:


Error: Provider produced invalid plan

Provider "null" planned an invalid value for
module.db.null_resource.db[0].triggers: planned value
cty.UnknownVal(cty.Map(cty.String)) does not match config value
cty.MapVal(map[string]cty.Value{"cluster_instance_ids":cty.UnknownVal(cty.String)}).

This is a bug in the provider, which should be reported in the provider's own
issue tracker.
