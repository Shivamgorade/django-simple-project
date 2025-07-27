import os
import openpyxl
from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime

def form_view(request):
    if request.method == 'POST':
        # Metadata
        date_time = request.POST.get('date_time')
        line_no = request.POST.get('line_no')
        shift = request.POST.get('shift')
        part_no = request.POST.get('part_no')
        part_type = request.POST.get('part_type')
        supervisor = request.POST.get('supervisor')

        # ST-15 Inputs
        dmc_st15 = request.POST.get('dmc_no')
        pos_501 = request.POST.get('POS_501')
        pos_502 = request.POST.get('POS_502')
        visual_staking_hu = request.POST.get('VISUAL_STAKING_HU')

        # ST-20 Inputs
        pos_311 = request.POST.get('pos311')
        pos_312 = request.POST.get('pos312')
        pos_411 = request.POST.get('pos411')
        pos_412 = request.POST.get('pos412')
        pos_531 = request.POST.get('pos531')
        pos_532 = request.POST.get('pos532')
        pos_541 = request.POST.get('pos541')
        pos_542 = request.POST.get('pos542')
        visual_staking_st20 = request.POST.get('visualStakingST20')

        # ST-25 Inputs
        pos_221 = request.POST.get('pos_221')
        visual_cbearing = request.POST.get('visual_cbearing')

        # ST-25 MV Staking
        pos201 = request.POST.get('pos201')
        pos202 = request.POST.get('pos202')
        pos211 = request.POST.get('pos211')
        pos212 = request.POST.get('pos212')
        visualStakingMV = request.POST.get('visualStakingMV')

        # ST-30 Motor Staking
        dmc_st30 = request.POST.get('dmc_st30')
        pos222 = request.POST.get('pos222')
        pos223 = request.POST.get('pos223')
        pos224 = request.POST.get('pos224')
        visual_staking_st30 = request.POST.get('visual_staking_st30')

        # ST-40 Inputs
        pos301 = request.POST.get('pos301')
        pos401 = request.POST.get('pos401')
        visualStakingST40 = request.POST.get('visualStakingST40')

        # ST-45 Inputs
        ecuScrewDamage = request.POST.get('ecuScrewDamage')
        pos231status = request.POST.get('pos231status')
        pos232status = request.POST.get('pos232status')

        # ST-85 Inputs
        ecuHousingDamage = request.POST.get('ecuHousingDamage')

        # LAST CHECKED BY Inputs
        checked_by = request.POST.get('checkedBy')

        # Excel path
        excel_path = os.path.join(settings.BASE_DIR, 'myapp', 'data', 'checksheet_data.xlsx')

        # Create or load workbook
        if os.path.exists(excel_path):
            workbook = openpyxl.load_workbook(excel_path)
            sheet = workbook.active
        else:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            headers = [
                'DATE & TIME', 'LINE NO', 'SHIFT', 'PART NO', 'PART TYPE', 'SUPERVISOR',

                # ST-15
                'ST15 DMC', 'POS 501 Depth', 'POS 502 Depth', 'Visual Staking HU (ST-15)',

                # ST-20
                'POS 311 Depth', 'POS 312 Depth', 'POS 411 Depth', 'POS 412 Depth',
                'POS 531 Depth', 'POS 532 Depth', 'POS 541 Depth', 'POS 542 Depth',
                'Visual Staking (ST-20)',

                # ST-25
                'ST25 DMC', 'Visual – C-Bearing',

                # ST-25 MV Staking
                'MV DMC', '201 Depth', '202 Depth', '211 Depth', '212 Depth', 'MV Visual',

                # ST-30 Motor Staking
                'ST30 DMC', '222 Depth', '223 Depth',
                '224 Depth', 'Visual Staking (ST-30)',

                # ST-40
                '301 Depth', '401 Depth', 'Visual Staking (ST-40)',

                # ST-45
                'Pos. 231 Status', 'Pos. 232 Status', 'ECU Screw Head Damage',

                # ST-85
                'ECU Housing Damage',

                # LAST CHECKED BY Inputs
                'Checked By',
            ]
            # Add header in row 1
            for col, header in enumerate(headers, start=1):
                sheet.cell(row=3, column=col, value=header)

        # Row data to insert
        row_data = [
            date_time, line_no, shift, part_no, part_type, supervisor,

            # ST-15
            dmc_st15, pos_501, pos_502, visual_staking_hu,

            # ST-20
            pos_311, pos_312, pos_411, pos_412,
            pos_531, pos_532, pos_541, pos_542,
            visual_staking_st20,

            # ST-25
            pos_221, visual_cbearing,

            # ST-25 MV Staking
            pos201, pos202, pos211, pos212, visualStakingMV,

            # ST-30 Motor Staking
            dmc_st30, pos222, pos223,
            pos224, visual_staking_st30,

            # ST-40
            pos301, pos401, visualStakingST40,

            # ST-45
            pos231status, pos232status, ecuScrewDamage,

            # ST-85
            ecuHousingDamage,

            # LAST CHECKED BY Inputs
            checked_by,
        ]

        # Find next available row from row 4 onward
        next_row = 4
        while sheet.cell(row=next_row, column=1).value:
            next_row += 1

        # Insert row data
        for col, value in enumerate(row_data, start=1):
            sheet.cell(row=next_row, column=col, value=value)

        # Save workbook
        workbook.save(excel_path)
        return redirect('form_view')

    return render(request, 'form.html')
