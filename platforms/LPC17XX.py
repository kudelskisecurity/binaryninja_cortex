from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="LPC17XX"
    ROM_OFF=0x00000000 
    RAM_OFF=0x10000000
    IRQ=MCU.IRQ+ [
        "NVIC_USB_IRQ",
        "NVIC_CAN_IRQ",
        "NVIC_GPDMA_IRQ",
        "NVIC_I2S_IRQ",
        "NVIC_EINT2_IRQ",
        "NVIC_EINT3_IRQ",
        "NVIC_ADC_IRQ",
        "NVIC_BOD_IRQ",
        "NVIC_ETHERNET_IRQ",
        "NVIC_RIT_IRQ",
        "NVIC_TIMER0_IRQ",
        "NVIC_WDT_IRQ",
        "NVIC_TIMER2_IRQ",
        "NVIC_TIMER1_IRQ",
        "NVIC_UART0_IRQ",
        "NVIC_TIMER3_IRQ",
        "NVIC_UART2_IRQ",
        "NVIC_UART1_IRQ",
        "NVIC_PWM_IRQ",
        "NVIC_UART3_IRQ",
        "NVIC_I2C1_IRQ",
        "NVIC_I2C0_IRQ",
        "NVIC_SPI_IRQ",
        "NVIC_I2C2_IRQ",
        "NVIC_SSP1_IRQ",
        "NVIC_SSP0_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_PLL0_IRQ",
        "NVIC_EINT1_IRQ",
        "NVIC_EINT0_IRQ",
        "NVIC_QEI_IRQ",
        "NVIC_MOTOR_PWM_IRQ",
        "NVIC_CAN_ACT_IRQ",
        "NVIC_USB_ACT_IRQ",
        "NVIC_PLL1_IRQ",
        ]
